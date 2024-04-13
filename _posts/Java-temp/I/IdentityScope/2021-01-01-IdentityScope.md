---
title: IdentityScope
permalink: /Java/IdentityScope/
date: 2021-01-11
key: Java.I.IdentityScope
category: Java
tags: ['java se', 'java.security', 'java.base', 'clase java', 'Java 1.1']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.I.IdentityScope.description }}

## Sintaxis
~~~java
@Deprecated(since="1.2", forRemoval=true) public abstract class IdentityScope extends Identity
~~~

## Constructores
* [IdentityScope()](/Java/IdentityScope/IdentityScope/)

## Métodos
* [addIdentity()](/Java/IdentityScope/addIdentity)
* [getIdentity()](/Java/IdentityScope/getIdentity)
* [getSystemScope()](/Java/IdentityScope/getSystemScope)
* [identities()](/Java/IdentityScope/identities)
* [removeIdentity()](/Java/IdentityScope/removeIdentity)
* [setSystemScope()](/Java/IdentityScope/setSystemScope)
* [size()](/Java/IdentityScope/size)
* [toString()](/Java/IdentityScope/toString)

## Ejemplo
~~~java
{{ site.data.Java.I.IdentityScope.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.IdentityScope.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
