---
title: TreeScanner
permalink: /Java/TreeScanner/
date: 2021-01-11
key: Java.T.TreeScanner
category: Java
tags: ['java se', 'com.sun.source.util', 'jdk.compiler', 'clase java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.T.TreeScanner.description }}

## Sintaxis
~~~java
public class TreeScanner<R,P> extends Object implements TreeVisitor<R,P>
~~~

## Constructores
* [TreeScanner()](/Java/TreeScanner/TreeScanner/)

## Métodos
* [reduce()](/Java/TreeScanner/reduce)
* [scan()](/Java/TreeScanner/scan)
* [visitAnnotatedType()](/Java/TreeScanner/visitAnnotatedType)
* [visitAnnotation()](/Java/TreeScanner/visitAnnotation)
* [visitArrayAccess()](/Java/TreeScanner/visitArrayAccess)
* [visitArrayType()](/Java/TreeScanner/visitArrayType)
* [visitAssert()](/Java/TreeScanner/visitAssert)
* [visitAssignment()](/Java/TreeScanner/visitAssignment)
* [visitBinary()](/Java/TreeScanner/visitBinary)
* [visitBlock()](/Java/TreeScanner/visitBlock)
* [visitBreak()](/Java/TreeScanner/visitBreak)
* [visitCase()](/Java/TreeScanner/visitCase)
* [visitCatch()](/Java/TreeScanner/visitCatch)
* [visitClass()](/Java/TreeScanner/visitClass)
* [visitCompilationUnit()](/Java/TreeScanner/visitCompilationUnit)
* [visitCompoundAssignment()](/Java/TreeScanner/visitCompoundAssignment)
* [visitConditionalExpression()](/Java/TreeScanner/visitConditionalExpression)
* [visitContinue()](/Java/TreeScanner/visitContinue)
* [visitDoWhileLoop()](/Java/TreeScanner/visitDoWhileLoop)
* [visitEmptyStatement()](/Java/TreeScanner/visitEmptyStatement)
* [visitEnhancedForLoop()](/Java/TreeScanner/visitEnhancedForLoop)
* [visitErroneous()](/Java/TreeScanner/visitErroneous)
* [visitExpressionStatement()](/Java/TreeScanner/visitExpressionStatement)
* [visitForLoop()](/Java/TreeScanner/visitForLoop)
* [visitIdentifier()](/Java/TreeScanner/visitIdentifier)
* [visitIf()](/Java/TreeScanner/visitIf)
* [visitImport()](/Java/TreeScanner/visitImport)
* [visitInstanceOf()](/Java/TreeScanner/visitInstanceOf)
* [visitIntersectionType()](/Java/TreeScanner/visitIntersectionType)
* [visitLabeledStatement()](/Java/TreeScanner/visitLabeledStatement)
* [visitLambdaExpression()](/Java/TreeScanner/visitLambdaExpression)
* [visitLiteral()](/Java/TreeScanner/visitLiteral)
* [visitMemberReference()](/Java/TreeScanner/visitMemberReference)
* [visitMemberSelect()](/Java/TreeScanner/visitMemberSelect)
* [visitMethod()](/Java/TreeScanner/visitMethod)
* [visitMethodInvocation()](/Java/TreeScanner/visitMethodInvocation)
* [visitModifiers()](/Java/TreeScanner/visitModifiers)
* [visitNewArray()](/Java/TreeScanner/visitNewArray)
* [visitNewClass()](/Java/TreeScanner/visitNewClass)
* [visitOther()](/Java/TreeScanner/visitOther)
* [visitPackage()](/Java/TreeScanner/visitPackage)
* [visitParameterizedType()](/Java/TreeScanner/visitParameterizedType)
* [visitParenthesized()](/Java/TreeScanner/visitParenthesized)
* [visitPrimitiveType()](/Java/TreeScanner/visitPrimitiveType)
* [visitReturn()](/Java/TreeScanner/visitReturn)
* [visitSwitch()](/Java/TreeScanner/visitSwitch)
* [visitSynchronized()](/Java/TreeScanner/visitSynchronized)
* [visitThrow()](/Java/TreeScanner/visitThrow)
* [visitTry()](/Java/TreeScanner/visitTry)
* [visitTypeCast()](/Java/TreeScanner/visitTypeCast)
* [visitTypeParameter()](/Java/TreeScanner/visitTypeParameter)
* [visitUnary()](/Java/TreeScanner/visitUnary)
* [visitUnionType()](/Java/TreeScanner/visitUnionType)
* [visitVariable()](/Java/TreeScanner/visitVariable)
* [visitWhileLoop()](/Java/TreeScanner/visitWhileLoop)
* [visitWildcard()](/Java/TreeScanner/visitWildcard)

## Ejemplo
~~~java
{{ site.data.Java.T.TreeScanner.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.TreeScanner.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
