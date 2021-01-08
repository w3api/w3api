---
title: DeclaredType
permalink: Java/DeclaredType
date: 2021-01-04
key: JavaJava.D.DeclaredType
category: java
tags: ['java se', 'javax.lang.model.type', 'java.compiler', 'interface java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.D.DeclaredType.description }}

## Sintaxis
~~~java
public interface DeclaredType extends ReferenceType
~~~

## Métodos
* [asElement()](/Java/DeclaredType/asElement)
* [getEnclosingType()](/Java/DeclaredType/getEnclosingType)
* [getTypeArguments()](/Java/DeclaredType/getTypeArguments)

## Ejemplo
~~~java
{{ site.data.Java.D.DeclaredType.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DeclaredType.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
