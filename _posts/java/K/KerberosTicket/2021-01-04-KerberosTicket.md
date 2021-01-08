---
title: KerberosTicket
permalink: Java/KerberosTicket
date: 2021-01-04
key: JavaJava.K.KerberosTicket
category: java
tags: ['java se', 'javax.security.auth.kerberos', 'java.security.jgss', 'clase java', 'Java 1.4']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.K.KerberosTicket.description }}

## Sintaxis
~~~java
public class KerberosTicket extends Object implements Destroyable, Refreshable, Serializable
~~~

## Constructores
* [KerberosTicket()](/Java/KerberosTicket/KerberosTicket/)

## Métodos
* [destroy()](/Java/KerberosTicket/destroy)
* [equals()](/Java/KerberosTicket/equals)
* [getAuthTime()](/Java/KerberosTicket/getAuthTime)
* [getClient()](/Java/KerberosTicket/getClient)
* [getClientAddresses()](/Java/KerberosTicket/getClientAddresses)
* [getEncoded()](/Java/KerberosTicket/getEncoded)
* [getEndTime()](/Java/KerberosTicket/getEndTime)
* [getFlags()](/Java/KerberosTicket/getFlags)
* [getRenewTill()](/Java/KerberosTicket/getRenewTill)
* [getServer()](/Java/KerberosTicket/getServer)
* [getSessionKey()](/Java/KerberosTicket/getSessionKey)
* [getSessionKeyType()](/Java/KerberosTicket/getSessionKeyType)
* [getStartTime()](/Java/KerberosTicket/getStartTime)
* [hashCode()](/Java/KerberosTicket/hashCode)
* [isCurrent()](/Java/KerberosTicket/isCurrent)
* [isDestroyed()](/Java/KerberosTicket/isDestroyed)
* [isForwardable()](/Java/KerberosTicket/isForwardable)
* [isForwarded()](/Java/KerberosTicket/isForwarded)
* [isInitial()](/Java/KerberosTicket/isInitial)
* [isPostdated()](/Java/KerberosTicket/isPostdated)
* [isProxiable()](/Java/KerberosTicket/isProxiable)
* [isProxy()](/Java/KerberosTicket/isProxy)
* [isRenewable()](/Java/KerberosTicket/isRenewable)
* [refresh()](/Java/KerberosTicket/refresh)
* [toString()](/Java/KerberosTicket/toString)

## Ejemplo
~~~java
{{ site.data.Java.K.KerberosTicket.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.K.KerberosTicket.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
