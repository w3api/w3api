---
title: ServicePermission
permalink: Java/ServicePermission
date: 2021-01-11
key: JavaJava.S.ServicePermission
category: java
tags: ['java se', 'javax.security.auth.kerberos', 'java.security.jgss', 'clase java', 'Java 1.4']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.ServicePermission.description }}

## Sintaxis
~~~java
public final class ServicePermission extends Permission implements Serializable
~~~

## Constructores
* [ServicePermission()](/Java/ServicePermission/ServicePermission/)

## Métodos
* [equals()](/Java/ServicePermission/equals)
* [getActions()](/Java/ServicePermission/getActions)
* [hashCode()](/Java/ServicePermission/hashCode)
* [implies()](/Java/ServicePermission/implies)
* [newPermissionCollection()](/Java/ServicePermission/newPermissionCollection)

## Ejemplo
~~~java
{{ site.data.Java.S.ServicePermission.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.ServicePermission.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
