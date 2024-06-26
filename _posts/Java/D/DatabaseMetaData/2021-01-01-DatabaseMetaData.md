---
title: DatabaseMetaData
permalink: /Java/DatabaseMetaData/
date: 2021-01-11
key: Java.D.DatabaseMetaData
category: Java
tags: ['java se', 'java.sql', 'java.sql', 'interface java', 'Java 1.1']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.D.DatabaseMetaData.description }}

## Sintaxis
~~~java
public interface DatabaseMetaData extends Wrapper
~~~

## Campos
* [attributeNoNulls](/Java/DatabaseMetaData/attributeNoNulls/)
* [attributeNullable](/Java/DatabaseMetaData/attributeNullable/)
* [attributeNullableUnknown](/Java/DatabaseMetaData/attributeNullableUnknown/)
* [bestRowNotPseudo](/Java/DatabaseMetaData/bestRowNotPseudo/)
* [bestRowPseudo](/Java/DatabaseMetaData/bestRowPseudo/)
* [bestRowSession](/Java/DatabaseMetaData/bestRowSession/)
* [bestRowTemporary](/Java/DatabaseMetaData/bestRowTemporary/)
* [bestRowTransaction](/Java/DatabaseMetaData/bestRowTransaction/)
* [bestRowUnknown](/Java/DatabaseMetaData/bestRowUnknown/)
* [columnNoNulls](/Java/DatabaseMetaData/columnNoNulls/)
* [columnNullable](/Java/DatabaseMetaData/columnNullable/)
* [columnNullableUnknown](/Java/DatabaseMetaData/columnNullableUnknown/)
* [functionColumnIn](/Java/DatabaseMetaData/functionColumnIn/)
* [functionColumnInOut](/Java/DatabaseMetaData/functionColumnInOut/)
* [functionColumnOut](/Java/DatabaseMetaData/functionColumnOut/)
* [functionColumnResult](/Java/DatabaseMetaData/functionColumnResult/)
* [functionColumnUnknown](/Java/DatabaseMetaData/functionColumnUnknown/)
* [functionNoNulls](/Java/DatabaseMetaData/functionNoNulls/)
* [functionNoTable](/Java/DatabaseMetaData/functionNoTable/)
* [functionNullable](/Java/DatabaseMetaData/functionNullable/)
* [functionNullableUnknown](/Java/DatabaseMetaData/functionNullableUnknown/)
* [functionResultUnknown](/Java/DatabaseMetaData/functionResultUnknown/)
* [functionReturn](/Java/DatabaseMetaData/functionReturn/)
* [functionReturnsTable](/Java/DatabaseMetaData/functionReturnsTable/)
* [importedKeyCascade](/Java/DatabaseMetaData/importedKeyCascade/)
* [importedKeyInitiallyDeferred](/Java/DatabaseMetaData/importedKeyInitiallyDeferred/)
* [importedKeyInitiallyImmediate](/Java/DatabaseMetaData/importedKeyInitiallyImmediate/)
* [importedKeyNoAction](/Java/DatabaseMetaData/importedKeyNoAction/)
* [importedKeyNotDeferrable](/Java/DatabaseMetaData/importedKeyNotDeferrable/)
* [importedKeyRestrict](/Java/DatabaseMetaData/importedKeyRestrict/)
* [importedKeySetDefault](/Java/DatabaseMetaData/importedKeySetDefault/)
* [importedKeySetNull](/Java/DatabaseMetaData/importedKeySetNull/)
* [procedureColumnIn](/Java/DatabaseMetaData/procedureColumnIn/)
* [procedureColumnInOut](/Java/DatabaseMetaData/procedureColumnInOut/)
* [procedureColumnOut](/Java/DatabaseMetaData/procedureColumnOut/)
* [procedureColumnResult](/Java/DatabaseMetaData/procedureColumnResult/)
* [procedureColumnReturn](/Java/DatabaseMetaData/procedureColumnReturn/)
* [procedureColumnUnknown](/Java/DatabaseMetaData/procedureColumnUnknown/)
* [procedureNoNulls](/Java/DatabaseMetaData/procedureNoNulls/)
* [procedureNoResult](/Java/DatabaseMetaData/procedureNoResult/)
* [procedureNullable](/Java/DatabaseMetaData/procedureNullable/)
* [procedureNullableUnknown](/Java/DatabaseMetaData/procedureNullableUnknown/)
* [procedureResultUnknown](/Java/DatabaseMetaData/procedureResultUnknown/)
* [procedureReturnsResult](/Java/DatabaseMetaData/procedureReturnsResult/)
* [sqlStateSQL](/Java/DatabaseMetaData/sqlStateSQL/)
* [sqlStateSQL99](/Java/DatabaseMetaData/sqlStateSQL99/)
* [sqlStateXOpen](/Java/DatabaseMetaData/sqlStateXOpen/)
* [tableIndexClustered](/Java/DatabaseMetaData/tableIndexClustered/)
* [tableIndexHashed](/Java/DatabaseMetaData/tableIndexHashed/)
* [tableIndexOther](/Java/DatabaseMetaData/tableIndexOther/)
* [tableIndexStatistic](/Java/DatabaseMetaData/tableIndexStatistic/)
* [typeNoNulls](/Java/DatabaseMetaData/typeNoNulls/)
* [typeNullable](/Java/DatabaseMetaData/typeNullable/)
* [typeNullableUnknown](/Java/DatabaseMetaData/typeNullableUnknown/)
* [typePredBasic](/Java/DatabaseMetaData/typePredBasic/)
* [typePredChar](/Java/DatabaseMetaData/typePredChar/)
* [typePredNone](/Java/DatabaseMetaData/typePredNone/)
* [typeSearchable](/Java/DatabaseMetaData/typeSearchable/)
* [versionColumnNotPseudo](/Java/DatabaseMetaData/versionColumnNotPseudo/)
* [versionColumnPseudo](/Java/DatabaseMetaData/versionColumnPseudo/)
* [versionColumnUnknown](/Java/DatabaseMetaData/versionColumnUnknown/)

## Métodos
* [allProceduresAreCallable()](/Java/DatabaseMetaData/allProceduresAreCallable/)
* [allTablesAreSelectable()](/Java/DatabaseMetaData/allTablesAreSelectable/)
* [autoCommitFailureClosesAllResultSets()](/Java/DatabaseMetaData/autoCommitFailureClosesAllResultSets/)
* [dataDefinitionCausesTransactionCommit()](/Java/DatabaseMetaData/dataDefinitionCausesTransactionCommit/)
* [dataDefinitionIgnoredInTransactions()](/Java/DatabaseMetaData/dataDefinitionIgnoredInTransactions/)
* [deletesAreDetected()](/Java/DatabaseMetaData/deletesAreDetected/)
* [doesMaxRowSizeIncludeBlobs()](/Java/DatabaseMetaData/doesMaxRowSizeIncludeBlobs/)
* [generatedKeyAlwaysReturned()](/Java/DatabaseMetaData/generatedKeyAlwaysReturned/)
* [getAttributes()](/Java/DatabaseMetaData/getAttributes/)
* [getBestRowIdentifier()](/Java/DatabaseMetaData/getBestRowIdentifier/)
* [getCatalogs()](/Java/DatabaseMetaData/getCatalogs/)
* [getCatalogSeparator()](/Java/DatabaseMetaData/getCatalogSeparator/)
* [getCatalogTerm()](/Java/DatabaseMetaData/getCatalogTerm/)
* [getClientInfoProperties()](/Java/DatabaseMetaData/getClientInfoProperties/)
* [getColumnPrivileges()](/Java/DatabaseMetaData/getColumnPrivileges/)
* [getColumns()](/Java/DatabaseMetaData/getColumns/)
* [getConnection()](/Java/DatabaseMetaData/getConnection/)
* [getCrossReference()](/Java/DatabaseMetaData/getCrossReference/)
* [getDatabaseMajorVersion()](/Java/DatabaseMetaData/getDatabaseMajorVersion/)
* [getDatabaseMinorVersion()](/Java/DatabaseMetaData/getDatabaseMinorVersion/)
* [getDatabaseProductName()](/Java/DatabaseMetaData/getDatabaseProductName/)
* [getDatabaseProductVersion()](/Java/DatabaseMetaData/getDatabaseProductVersion/)
* [getDefaultTransactionIsolation()](/Java/DatabaseMetaData/getDefaultTransactionIsolation/)
* [getDriverMajorVersion()](/Java/DatabaseMetaData/getDriverMajorVersion/)
* [getDriverMinorVersion()](/Java/DatabaseMetaData/getDriverMinorVersion/)
* [getDriverName()](/Java/DatabaseMetaData/getDriverName/)
* [getDriverVersion()](/Java/DatabaseMetaData/getDriverVersion/)
* [getExportedKeys()](/Java/DatabaseMetaData/getExportedKeys/)
* [getExtraNameCharacters()](/Java/DatabaseMetaData/getExtraNameCharacters/)
* [getFunctionColumns()](/Java/DatabaseMetaData/getFunctionColumns/)
* [getFunctions()](/Java/DatabaseMetaData/getFunctions/)
* [getIdentifierQuoteString()](/Java/DatabaseMetaData/getIdentifierQuoteString/)
* [getImportedKeys()](/Java/DatabaseMetaData/getImportedKeys/)
* [getIndexInfo()](/Java/DatabaseMetaData/getIndexInfo/)
* [getJDBCMajorVersion()](/Java/DatabaseMetaData/getJDBCMajorVersion/)
* [getJDBCMinorVersion()](/Java/DatabaseMetaData/getJDBCMinorVersion/)
* [getMaxBinaryLiteralLength()](/Java/DatabaseMetaData/getMaxBinaryLiteralLength/)
* [getMaxCatalogNameLength()](/Java/DatabaseMetaData/getMaxCatalogNameLength/)
* [getMaxCharLiteralLength()](/Java/DatabaseMetaData/getMaxCharLiteralLength/)
* [getMaxColumnNameLength()](/Java/DatabaseMetaData/getMaxColumnNameLength/)
* [getMaxColumnsInGroupBy()](/Java/DatabaseMetaData/getMaxColumnsInGroupBy/)
* [getMaxColumnsInIndex()](/Java/DatabaseMetaData/getMaxColumnsInIndex/)
* [getMaxColumnsInOrderBy()](/Java/DatabaseMetaData/getMaxColumnsInOrderBy/)
* [getMaxColumnsInSelect()](/Java/DatabaseMetaData/getMaxColumnsInSelect/)
* [getMaxColumnsInTable()](/Java/DatabaseMetaData/getMaxColumnsInTable/)
* [getMaxConnections()](/Java/DatabaseMetaData/getMaxConnections/)
* [getMaxCursorNameLength()](/Java/DatabaseMetaData/getMaxCursorNameLength/)
* [getMaxIndexLength()](/Java/DatabaseMetaData/getMaxIndexLength/)
* [getMaxLogicalLobSize()](/Java/DatabaseMetaData/getMaxLogicalLobSize/)
* [getMaxProcedureNameLength()](/Java/DatabaseMetaData/getMaxProcedureNameLength/)
* [getMaxRowSize()](/Java/DatabaseMetaData/getMaxRowSize/)
* [getMaxSchemaNameLength()](/Java/DatabaseMetaData/getMaxSchemaNameLength/)
* [getMaxStatementLength()](/Java/DatabaseMetaData/getMaxStatementLength/)
* [getMaxStatements()](/Java/DatabaseMetaData/getMaxStatements/)
* [getMaxTableNameLength()](/Java/DatabaseMetaData/getMaxTableNameLength/)
* [getMaxTablesInSelect()](/Java/DatabaseMetaData/getMaxTablesInSelect/)
* [getMaxUserNameLength()](/Java/DatabaseMetaData/getMaxUserNameLength/)
* [getNumericFunctions()](/Java/DatabaseMetaData/getNumericFunctions/)
* [getPrimaryKeys()](/Java/DatabaseMetaData/getPrimaryKeys/)
* [getProcedureColumns()](/Java/DatabaseMetaData/getProcedureColumns/)
* [getProcedures()](/Java/DatabaseMetaData/getProcedures/)
* [getProcedureTerm()](/Java/DatabaseMetaData/getProcedureTerm/)
* [getPseudoColumns()](/Java/DatabaseMetaData/getPseudoColumns/)
* [getResultSetHoldability()](/Java/DatabaseMetaData/getResultSetHoldability/)
* [getRowIdLifetime()](/Java/DatabaseMetaData/getRowIdLifetime/)
* [getSchemas()](/Java/DatabaseMetaData/getSchemas/)
* [getSchemaTerm()](/Java/DatabaseMetaData/getSchemaTerm/)
* [getSearchStringEscape()](/Java/DatabaseMetaData/getSearchStringEscape/)
* [getSQLKeywords()](/Java/DatabaseMetaData/getSQLKeywords/)
* [getSQLStateType()](/Java/DatabaseMetaData/getSQLStateType/)
* [getStringFunctions()](/Java/DatabaseMetaData/getStringFunctions/)
* [getSuperTables()](/Java/DatabaseMetaData/getSuperTables/)
* [getSuperTypes()](/Java/DatabaseMetaData/getSuperTypes/)
* [getSystemFunctions()](/Java/DatabaseMetaData/getSystemFunctions/)
* [getTablePrivileges()](/Java/DatabaseMetaData/getTablePrivileges/)
* [getTables()](/Java/DatabaseMetaData/getTables/)
* [getTableTypes()](/Java/DatabaseMetaData/getTableTypes/)
* [getTimeDateFunctions()](/Java/DatabaseMetaData/getTimeDateFunctions/)
* [getTypeInfo()](/Java/DatabaseMetaData/getTypeInfo/)
* [getUDTs()](/Java/DatabaseMetaData/getUDTs/)
* [getURL()](/Java/DatabaseMetaData/getURL/)
* [getUserName()](/Java/DatabaseMetaData/getUserName/)
* [getVersionColumns()](/Java/DatabaseMetaData/getVersionColumns/)
* [insertsAreDetected()](/Java/DatabaseMetaData/insertsAreDetected/)
* [isCatalogAtStart()](/Java/DatabaseMetaData/isCatalogAtStart/)
* [isReadOnly()](/Java/DatabaseMetaData/isReadOnly/)
* [locatorsUpdateCopy()](/Java/DatabaseMetaData/locatorsUpdateCopy/)
* [nullPlusNonNullIsNull()](/Java/DatabaseMetaData/nullPlusNonNullIsNull/)
* [nullsAreSortedAtEnd()](/Java/DatabaseMetaData/nullsAreSortedAtEnd/)
* [nullsAreSortedAtStart()](/Java/DatabaseMetaData/nullsAreSortedAtStart/)
* [nullsAreSortedHigh()](/Java/DatabaseMetaData/nullsAreSortedHigh/)
* [nullsAreSortedLow()](/Java/DatabaseMetaData/nullsAreSortedLow/)
* [othersDeletesAreVisible()](/Java/DatabaseMetaData/othersDeletesAreVisible/)
* [othersInsertsAreVisible()](/Java/DatabaseMetaData/othersInsertsAreVisible/)
* [othersUpdatesAreVisible()](/Java/DatabaseMetaData/othersUpdatesAreVisible/)
* [ownDeletesAreVisible()](/Java/DatabaseMetaData/ownDeletesAreVisible/)
* [ownInsertsAreVisible()](/Java/DatabaseMetaData/ownInsertsAreVisible/)
* [ownUpdatesAreVisible()](/Java/DatabaseMetaData/ownUpdatesAreVisible/)
* [storesLowerCaseIdentifiers()](/Java/DatabaseMetaData/storesLowerCaseIdentifiers/)
* [storesLowerCaseQuotedIdentifiers()](/Java/DatabaseMetaData/storesLowerCaseQuotedIdentifiers/)
* [storesMixedCaseIdentifiers()](/Java/DatabaseMetaData/storesMixedCaseIdentifiers/)
* [storesMixedCaseQuotedIdentifiers()](/Java/DatabaseMetaData/storesMixedCaseQuotedIdentifiers/)
* [storesUpperCaseIdentifiers()](/Java/DatabaseMetaData/storesUpperCaseIdentifiers/)
* [storesUpperCaseQuotedIdentifiers()](/Java/DatabaseMetaData/storesUpperCaseQuotedIdentifiers/)
* [supportsAlterTableWithAddColumn()](/Java/DatabaseMetaData/supportsAlterTableWithAddColumn/)
* [supportsAlterTableWithDropColumn()](/Java/DatabaseMetaData/supportsAlterTableWithDropColumn/)
* [supportsANSI92EntryLevelSQL()](/Java/DatabaseMetaData/supportsANSI92EntryLevelSQL/)
* [supportsANSI92FullSQL()](/Java/DatabaseMetaData/supportsANSI92FullSQL/)
* [supportsANSI92IntermediateSQL()](/Java/DatabaseMetaData/supportsANSI92IntermediateSQL/)
* [supportsBatchUpdates()](/Java/DatabaseMetaData/supportsBatchUpdates/)
* [supportsCatalogsInDataManipulation()](/Java/DatabaseMetaData/supportsCatalogsInDataManipulation/)
* [supportsCatalogsInIndexDefinitions()](/Java/DatabaseMetaData/supportsCatalogsInIndexDefinitions/)
* [supportsCatalogsInPrivilegeDefinitions()](/Java/DatabaseMetaData/supportsCatalogsInPrivilegeDefinitions/)
* [supportsCatalogsInProcedureCalls()](/Java/DatabaseMetaData/supportsCatalogsInProcedureCalls/)
* [supportsCatalogsInTableDefinitions()](/Java/DatabaseMetaData/supportsCatalogsInTableDefinitions/)
* [supportsColumnAliasing()](/Java/DatabaseMetaData/supportsColumnAliasing/)
* [supportsConvert()](/Java/DatabaseMetaData/supportsConvert/)
* [supportsCoreSQLGrammar()](/Java/DatabaseMetaData/supportsCoreSQLGrammar/)
* [supportsCorrelatedSubqueries()](/Java/DatabaseMetaData/supportsCorrelatedSubqueries/)
* [supportsDataDefinitionAndDataManipulationTransactions()](/Java/DatabaseMetaData/supportsDataDefinitionAndDataManipulationTransactions/)
* [supportsDataManipulationTransactionsOnly()](/Java/DatabaseMetaData/supportsDataManipulationTransactionsOnly/)
* [supportsDifferentTableCorrelationNames()](/Java/DatabaseMetaData/supportsDifferentTableCorrelationNames/)
* [supportsExpressionsInOrderBy()](/Java/DatabaseMetaData/supportsExpressionsInOrderBy/)
* [supportsExtendedSQLGrammar()](/Java/DatabaseMetaData/supportsExtendedSQLGrammar/)
* [supportsFullOuterJoins()](/Java/DatabaseMetaData/supportsFullOuterJoins/)
* [supportsGetGeneratedKeys()](/Java/DatabaseMetaData/supportsGetGeneratedKeys/)
* [supportsGroupBy()](/Java/DatabaseMetaData/supportsGroupBy/)
* [supportsGroupByBeyondSelect()](/Java/DatabaseMetaData/supportsGroupByBeyondSelect/)
* [supportsGroupByUnrelated()](/Java/DatabaseMetaData/supportsGroupByUnrelated/)
* [supportsIntegrityEnhancementFacility()](/Java/DatabaseMetaData/supportsIntegrityEnhancementFacility/)
* [supportsLikeEscapeClause()](/Java/DatabaseMetaData/supportsLikeEscapeClause/)
* [supportsLimitedOuterJoins()](/Java/DatabaseMetaData/supportsLimitedOuterJoins/)
* [supportsMinimumSQLGrammar()](/Java/DatabaseMetaData/supportsMinimumSQLGrammar/)
* [supportsMixedCaseIdentifiers()](/Java/DatabaseMetaData/supportsMixedCaseIdentifiers/)
* [supportsMixedCaseQuotedIdentifiers()](/Java/DatabaseMetaData/supportsMixedCaseQuotedIdentifiers/)
* [supportsMultipleOpenResults()](/Java/DatabaseMetaData/supportsMultipleOpenResults/)
* [supportsMultipleResultSets()](/Java/DatabaseMetaData/supportsMultipleResultSets/)
* [supportsMultipleTransactions()](/Java/DatabaseMetaData/supportsMultipleTransactions/)
* [supportsNamedParameters()](/Java/DatabaseMetaData/supportsNamedParameters/)
* [supportsNonNullableColumns()](/Java/DatabaseMetaData/supportsNonNullableColumns/)
* [supportsOpenCursorsAcrossCommit()](/Java/DatabaseMetaData/supportsOpenCursorsAcrossCommit/)
* [supportsOpenCursorsAcrossRollback()](/Java/DatabaseMetaData/supportsOpenCursorsAcrossRollback/)
* [supportsOpenStatementsAcrossCommit()](/Java/DatabaseMetaData/supportsOpenStatementsAcrossCommit/)
* [supportsOpenStatementsAcrossRollback()](/Java/DatabaseMetaData/supportsOpenStatementsAcrossRollback/)
* [supportsOrderByUnrelated()](/Java/DatabaseMetaData/supportsOrderByUnrelated/)
* [supportsOuterJoins()](/Java/DatabaseMetaData/supportsOuterJoins/)
* [supportsPositionedDelete()](/Java/DatabaseMetaData/supportsPositionedDelete/)
* [supportsPositionedUpdate()](/Java/DatabaseMetaData/supportsPositionedUpdate/)
* [supportsRefCursors()](/Java/DatabaseMetaData/supportsRefCursors/)
* [supportsResultSetConcurrency()](/Java/DatabaseMetaData/supportsResultSetConcurrency/)
* [supportsResultSetHoldability()](/Java/DatabaseMetaData/supportsResultSetHoldability/)
* [supportsResultSetType()](/Java/DatabaseMetaData/supportsResultSetType/)
* [supportsSavepoints()](/Java/DatabaseMetaData/supportsSavepoints/)
* [supportsSchemasInDataManipulation()](/Java/DatabaseMetaData/supportsSchemasInDataManipulation/)
* [supportsSchemasInIndexDefinitions()](/Java/DatabaseMetaData/supportsSchemasInIndexDefinitions/)
* [supportsSchemasInPrivilegeDefinitions()](/Java/DatabaseMetaData/supportsSchemasInPrivilegeDefinitions/)
* [supportsSchemasInProcedureCalls()](/Java/DatabaseMetaData/supportsSchemasInProcedureCalls/)
* [supportsSchemasInTableDefinitions()](/Java/DatabaseMetaData/supportsSchemasInTableDefinitions/)
* [supportsSelectForUpdate()](/Java/DatabaseMetaData/supportsSelectForUpdate/)
* [supportsSharding()](/Java/DatabaseMetaData/supportsSharding/)
* [supportsStatementPooling()](/Java/DatabaseMetaData/supportsStatementPooling/)
* [supportsStoredFunctionsUsingCallSyntax()](/Java/DatabaseMetaData/supportsStoredFunctionsUsingCallSyntax/)
* [supportsStoredProcedures()](/Java/DatabaseMetaData/supportsStoredProcedures/)
* [supportsSubqueriesInComparisons()](/Java/DatabaseMetaData/supportsSubqueriesInComparisons/)
* [supportsSubqueriesInExists()](/Java/DatabaseMetaData/supportsSubqueriesInExists/)
* [supportsSubqueriesInIns()](/Java/DatabaseMetaData/supportsSubqueriesInIns/)
* [supportsSubqueriesInQuantifieds()](/Java/DatabaseMetaData/supportsSubqueriesInQuantifieds/)
* [supportsTableCorrelationNames()](/Java/DatabaseMetaData/supportsTableCorrelationNames/)
* [supportsTransactionIsolationLevel()](/Java/DatabaseMetaData/supportsTransactionIsolationLevel/)
* [supportsTransactions()](/Java/DatabaseMetaData/supportsTransactions/)
* [supportsUnion()](/Java/DatabaseMetaData/supportsUnion/)
* [supportsUnionAll()](/Java/DatabaseMetaData/supportsUnionAll/)
* [updatesAreDetected()](/Java/DatabaseMetaData/updatesAreDetected/)
* [usesLocalFilePerTable()](/Java/DatabaseMetaData/usesLocalFilePerTable/)
* [usesLocalFiles()](/Java/DatabaseMetaData/usesLocalFiles/)

## Ejemplo
~~~java
{{ site.data.Java.D.DatabaseMetaData.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DatabaseMetaData.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
