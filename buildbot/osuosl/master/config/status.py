import os
import buildbot
import buildbot.status.html
import buildbot.status.mail
import buildbot.status.words

import config
from zorg.buildbot.util.ConfigEmailLookup import ConfigEmailLookup
from zorg.buildbot.util.InformativeMailNotifier import InformativeMailNotifier

# Returns a list of Status Targets. The results of each build will be
# pushed to these targets. buildbot/status/*.py has a variety to choose from,
# including web pages, email senders, and IRC bots.

def get_status_targets(standard_builders, standard_categories=None):

    from buildbot.status import html
    from buildbot.status.web import auth, authz
    authz_cfg=authz.Authz(
                      # change any of these to True to enable; see the manual for more
                      # options
                      gracefulShutdown   = False,
                      forceBuild         = True, # use this to test your slave once it is set up
                      forceAllBuilds     = False,
                      pingBuilder        = True,
                      stopBuild          = True,
                      stopAllBuilds      = False,
                      cancelPendingBuild = True,
                      )

    default_email = config.options.get('Master Options', 'default_email')

    return [
        buildbot.status.html.WebStatus(
            http_port = 8011, authz=authz_cfg),

        # All the standard builders send e-mail and IRC notifications.
        buildbot.status.mail.MailNotifier(
            fromaddr = "llvm.buildmaster@lab.llvm.org",
            lookup = ConfigEmailLookup(os.path.join(os.path.dirname(__file__),
                                                    "llvmauthors.cfg"),
                                       default_email),
            mode = "problem",
            builders = standard_builders),
        buildbot.status.words.IRC(
            host = "irc.oftc.net", nick = "llvmbb", channels = ["#llvm"],
            allowForce = True,
            categories = standard_categories,
            notify_events = ['successToFailure', 'failureToSuccess']),

        # In addition to that the following notifiers are defined for special
        # cases.
        InformativeMailNotifier(
            fromaddr = "llvm.buildmaster@lab.llvm.org",
            sendToInterestedUsers= False,
            extraRecipients = ["tobias@grosser.es"],
            subject="Build %(builder)s Failure",
            mode = "failing",
            builders = ["polly-amd64-linux", "polly-intel32-linux",
                        "polly-perf-O3", "polly-perf-O3-polly",
                        "polly-perf-O3-polly-codegen-isl",
                        "polly-perf-O3-polly-scev",
                        "polly-perf-O3-polly-scev-codegen-isl",
                        "polly-perf-O3-polly-detect"],
            addLogs=False,
            num_lines = 15),
        InformativeMailNotifier(
            fromaddr = "llvm.buildmaster@lab.llvm.org",
            sendToInterestedUsers= False,
            extraRecipients = ["dblaikie@gmail.com", "echristo@gmail.com",
                               "daniel.malea@intel.com", "matt.kopec@intel.com",
                               "andrew.kaylor@intel.com", "ashok.thirumurthi@intel.com"],
            subject="Build %(builder)s Failure",
            mode = "failing",
            builders = ["clang-x86_64-darwin10-gdb", "clang-x86_64-ubuntu-gdb-75"],
            addLogs=False,
            num_lines = 15),
        InformativeMailNotifier(
            fromaddr = "llvm.buildmaster@lab.llvm.org",
            sendToInterestedUsers= False,
            extraRecipients = ["gribozavr@gmail.com"],
            subject="Build %(builder)s Failure",
            mode = "failing",
            builders = ["clang-x86_64-debian-fast"],
            addLogs=False,
            num_lines = 15),
        InformativeMailNotifier(
            fromaddr = "llvm.buildmaster@lab.llvm.org",
            sendToInterestedUsers= False,
            extraRecipients = ["mstester.llvm@gmail.com"],
            subject="Build %(builder)s Failure",
            mode = "failing",
            builders = ["clang-atom-d525-fedora", "clang-atom-d525-fedora-rel",
                        "clang-x64-ninja-win7"],
            addLogs=False,
            num_lines = 15),
        InformativeMailNotifier(
            fromaddr = "llvm.buildmaster@lab.llvm.org",
            sendToInterestedUsers= False,
            extraRecipients = ["llvm.buildmaster@quicinc.com"],
            subject="Build %(builder)s Failure",
            mode = "failing",
            builders = ["llvm-hexagon-elf","clang-hexagon-elf"],
            addLogs=False,
            num_lines = 15),
        InformativeMailNotifier(
            fromaddr = "llvm.buildmaster@lab.llvm.org",
            sendToInterestedUsers= False,
            extraRecipients = ["Ulrich.Weigand@de.ibm.com"],
            subject="Build %(builder)s Failure",
            mode = "failing",
            builders = ["clang-s390x-linux"],
            addLogs=False,
            num_lines = 15),
        InformativeMailNotifier(
            fromaddr = "llvm.buildmaster@lab.llvm.org",
            sendToInterestedUsers= False,
            extraRecipients = ["axwalk@gmail.com","peter@pcc.me.uk"],
            subject="Build %(builder)s Failure",
            mode = "failing",
            builders = ["llgo-x86_64-linux"],
            addLogs=False,
            num_lines = 15),
        InformativeMailNotifier(
            fromaddr = "llvm.buildmaster@lab.llvm.org",
            sendToInterestedUsers= False,
            extraRecipients = ["lldb-build-police-gmt@grotations.appspotmail.com",
                               "lldb-build-police-pst@grotations.appspotmail.com"],
            subject="Build %(builder)s Failure",
            mode = "failing",
            builders = ["lldb-x86_64-ubuntu-14.04-cmake",
                        "lldb-x86_64-ubuntu-14.04-buildserver",
                        "lldb-windows7-android",
                        "lldb-x86_64-darwin-13.4",
                        "lldb-x86_64-ubuntu-14.04-android"],
            addLogs=False,
            num_lines = 15),
        InformativeMailNotifier(
            fromaddr = "llvm.buildmaster@lab.llvm.org",
            sendToInterestedUsers= False,
            extraRecipients = ["sunil_srivastava@playstation.sony.com",
                               "warren_ristow@playstation.sony.com"],
            subject="Build %(builder)s Failure",
            mode = "failing",
            builders = ["clang-x86_64-linux-abi-test"],
            addLogs=False,
            num_lines = 15),
        InformativeMailNotifier(
            fromaddr = "llvm.buildmaster@lab.llvm.org",
            sendToInterestedUsers= False,
            extraRecipients = ["vasileios.kalintiris@imgtec.com"],
            subject="Build %(builder)s Failure",
            mode = "failing",
            builders = ["llvm-mips-linux", "clang-cmake-mips",
                        "clang-cmake-mipsel"],
            addLogs=False,
            num_lines = 15),
        InformativeMailNotifier(
            fromaddr = "llvm.buildmaster@lab.llvm.org",
            sendToInterestedUsers= False,
            extraRecipients = ["gkistanova@gmail.com"],
            subject="Build %(builder)s Failure",
            mode = "failing",
            builders = ["lld-x86_64-win7", "clang-x86_64-linux-abi-test",
                        "lld-x86_64-freebsd", "sanitizer_x86_64-freebsd",
                        "lld-x86_64-darwin13", "clang-3stage-ubuntu",
                        "llvm-clang-lld-x86_64-scei-ps4-ubuntu-fast",
                        "llvm-clang-lld-x86_64-scei-ps4-windows10pro-fast",
                        "clang-with-lto-ubuntu"],
            addLogs=False),
        ]
