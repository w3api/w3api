---
title: KerberosPrincipal
permalink: Java/KerberosPrincipal
date: 2021-01-11
key: JavaJava.K.KerberosPrincipal
category: java
tags: ['java se', 'javax.security.auth.kerberos', 'java.security.jgss', 'clase java', 'Java 1.4']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.K.KerberosPrincipal.description }}

## Sintaxis
~~~java
public final class KerberosPrincipal extends Object implements Principal, Serializable
~~~

## Constructores
* [KerberosPrincipal()](/Java/KerberosPrincipal/KerberosPrincipal/)

## Campos
* [KRB_NT_PRINCIPAL](/Java/KerberosPrincipal/KRB_NT_PRINCIPAL)
* [KRB_NT_SRV_HST](/Java/KerberosPrincipal/KRB_NT_SRV_HST)
* [KRB_NT_SRV_INST](/Java/KerberosPrincipal/KRB_NT_SRV_INST)
* [KRB_NT_SRV_XHST](/Java/KerberosPrincipal/KRB_NT_SRV_XHST)
* [KRB_NT_UID](/Java/KerberosPrincipal/KRB_NT_UID)
* [KRB_NT_UNKNOWN](/Java/KerberosPrincipal/KRB_NT_UNKNOWN)

## Métodos
* [equals()](/Java/KerberosPrincipal/equals)
* [getName()](/Java/KerberosPrincipal/getName)
* [getNameType()](/Java/KerberosPrincipal/getNameType)
* [getRealm()](/Java/KerberosPrincipal/getRealm)
* [hashCode()](/Java/KerberosPrincipal/hashCode)
* [toString()](/Java/KerberosPrincipal/toString)

## Ejemplo
~~~java
{{ site.data.Java.K.KerberosPrincipal.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.K.KerberosPrincipal.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
