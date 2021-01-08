---
title: DelegationPermission
permalink: Java/DelegationPermission
date: 2021-01-04
key: JavaJava.D.DelegationPermission
category: java
tags: ['java se', 'javax.security.auth.kerberos', 'java.security.jgss', 'clase java', 'Java 1.4']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.D.DelegationPermission.description }}

## Sintaxis
~~~java
public final class DelegationPermission extends BasicPermission implements Serializable
~~~

## Constructores
* [DelegationPermission()](/Java/DelegationPermission/DelegationPermission/)

## Métodos
* [equals()](/Java/DelegationPermission/equals)
* [hashCode()](/Java/DelegationPermission/hashCode)
* [implies()](/Java/DelegationPermission/implies)
* [newPermissionCollection()](/Java/DelegationPermission/newPermissionCollection)

## Ejemplo
~~~java
{{ site.data.Java.D.DelegationPermission.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DelegationPermission.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
