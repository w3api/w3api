---
title: GSSContext
permalink: /Java/GSSContext/
date: 2021-01-11
key: Java.G.GSSContext
category: Java
tags: ['java se', 'org.ietf.jgss', 'java.security.jgss', 'interface java', 'Java 1.4']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.G.GSSContext.description }}

## Sintaxis
~~~java
public interface GSSContext
~~~

## Campos
* [DEFAULT_LIFETIME](/Java/GSSContext/DEFAULT_LIFETIME)
* [INDEFINITE_LIFETIME](/Java/GSSContext/INDEFINITE_LIFETIME)

## Métodos
* [acceptSecContext()](/Java/GSSContext/acceptSecContext)
* [dispose()](/Java/GSSContext/dispose)
* [export()](/Java/GSSContext/export)
* [getAnonymityState()](/Java/GSSContext/getAnonymityState)
* [getConfState()](/Java/GSSContext/getConfState)
* [getCredDelegState()](/Java/GSSContext/getCredDelegState)
* [getDelegCred()](/Java/GSSContext/getDelegCred)
* [getIntegState()](/Java/GSSContext/getIntegState)
* [getLifetime()](/Java/GSSContext/getLifetime)
* [getMech()](/Java/GSSContext/getMech)
* [getMIC()](/Java/GSSContext/getMIC)
* [getMutualAuthState()](/Java/GSSContext/getMutualAuthState)
* [getReplayDetState()](/Java/GSSContext/getReplayDetState)
* [getSequenceDetState()](/Java/GSSContext/getSequenceDetState)
* [getSrcName()](/Java/GSSContext/getSrcName)
* [getTargName()](/Java/GSSContext/getTargName)
* [getWrapSizeLimit()](/Java/GSSContext/getWrapSizeLimit)
* [initSecContext()](/Java/GSSContext/initSecContext)
* [isEstablished()](/Java/GSSContext/isEstablished)
* [isInitiator()](/Java/GSSContext/isInitiator)
* [isProtReady()](/Java/GSSContext/isProtReady)
* [isTransferable()](/Java/GSSContext/isTransferable)
* [requestAnonymity()](/Java/GSSContext/requestAnonymity)
* [requestConf()](/Java/GSSContext/requestConf)
* [requestCredDeleg()](/Java/GSSContext/requestCredDeleg)
* [requestInteg()](/Java/GSSContext/requestInteg)
* [requestLifetime()](/Java/GSSContext/requestLifetime)
* [requestMutualAuth()](/Java/GSSContext/requestMutualAuth)
* [requestReplayDet()](/Java/GSSContext/requestReplayDet)
* [requestSequenceDet()](/Java/GSSContext/requestSequenceDet)
* [setChannelBinding()](/Java/GSSContext/setChannelBinding)
* [unwrap()](/Java/GSSContext/unwrap)
* [verifyMIC()](/Java/GSSContext/verifyMIC)
* [wrap()](/Java/GSSContext/wrap)

## Ejemplo
~~~java
{{ site.data.Java.G.GSSContext.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.G.GSSContext.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
