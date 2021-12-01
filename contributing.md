Important notes about Git

"git clone" makes a local repository (decentralized) from the cloud server (GitHub).   

A .git directory contains a local database (see illustration) that keeps track of local changes, "git commit" makes a child of the original parent on the local directory.  Git commits over time are a series of SHA's.

A .gitignore file tells .git to ignore certain files in directory tree (ie .idea)

The "git push" command moves files from local system back to cloud server (GitHub)

Often a merge is required as a decentralized system has many simultaneous contributors.

Git branches and/or forks can be used to push code to  isolated locations to on the server/cloud.  This simply delays the inevitable merge, but has benefit of keeping main branch of project stable.

Pull requests is common process used to merge code from isolated branches to main branch.
