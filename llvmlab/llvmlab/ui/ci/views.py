import flask
from flask import abort
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for
from flask import current_app
ci = flask.Module(__name__, url_prefix='/ci')

from llvmlab.ci import config

# Hard-coded current configuration.
#
# FIXME: Figure out how to get as much of this as possible dynamically. One
# problem is how do we deal with changes to the CI infrastructure? Should we
# load a config object per-revision, and try to be smart about caching it unless
# things change? Can we report results across changing configs?
phases = [
    config.Phase("Sanity", 1, []),
    config.Phase("Living On", 2, []),
    config.Phase("Tree Health", 3, []),
    config.Phase("Validation", 4, [])]
builders = [
    config.Builder("clang-x86_64-osx10-gcc42-RA"),
    config.Builder("clang-x86_64-osx10-DA"),
    config.Builder("clang-x86_64-osx10-RA"),
    config.Builder("nightly_clang-x86_64-osx10-gcc42-RA"),
    config.Builder("nightly_clang-x86_64-osx10-DA"),
    config.Builder("nightly_clang-x86_64-osx10-RA"),
    config.Builder("nightly_clang-x86_64-osx10-RA-O0"),
    config.Builder("nightly_clang-x86_64-osx10-RA-Os"),
    config.Builder("nightly_clang-x86_64-osx10-RA-O3"),
    config.Builder("nightly_clang-x86_64-osx10-RA-flto"),
    config.Builder("nightly_clang-x86_64-osx10-RA-g"),
    config.Builder("clang-x86_64-osx10-RA-stage3"),
    config.Builder("gccTestSuite-clang-x86_64-osx10-RA"),
    config.Builder("nightly_clang-x86_64-osx10-RA-stage3-g"),
    config.Builder("libcxx-clang-x86_64-osx10-RA"),
    config.Builder("boost-trunk-clang-x86_64-osx10-RA")]
published_builds = [
    config.PublishedBuild("LLVM", "Linux", "i386", "llvm-linux-i386.tgz"),
    config.PublishedBuild("LLVM", "Mac OS X (SnowLeopard)", "x86_64",
                          "llvm-darwin10-x86_64.tgz"),

    config.PublishedBuild("Clang", "Linux", "i386", "clang-linux-i386.tgz"),
    config.PublishedBuild("Clang", "Linux", "x86_64", "clang-linux-x86_64.tgz"),
    config.PublishedBuild("Clang", "Mac OS X (SnowLeopard)", "x86_64",
                          "clang-darwin10-x86_64.tgz"),
    config.PublishedBuild("Clang", "Windows", "i386", "clang-windows-i386.tgz"),

    config.PublishedBuild("llvm-gcc-4.2", "Linux", "i386",
                          "llvm-gcc-4.2-linux-i386.tgz"),
    config.PublishedBuild("llvm-gcc-4.2", "Linux", "x86_64",
                          "llvm-gcc-4.2-linux-x86_64.tgz")]
g_config = config.Config(phases, builders, published_builds)

@ci.route('/')
def dashboard():
    return render_template("dashboard.html", ci_config=g_config)

