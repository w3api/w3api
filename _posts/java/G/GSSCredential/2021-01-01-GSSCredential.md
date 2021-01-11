---
title: GSSCredential
permalink: Java/GSSCredential
date: 2021-01-11
key: JavaJava.G.GSSCredential
category: java
tags: ['java se', 'org.ietf.jgss', 'java.security.jgss', 'interface java', 'Java 1.4']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.G.GSSCredential.description }}

## Sintaxis
~~~java
public interface GSSCredential extends Cloneable
~~~

## Campos
* [ACCEPT_ONLY](/Java/GSSCredential/ACCEPT_ONLY)
* [DEFAULT_LIFETIME](/Java/GSSCredential/DEFAULT_LIFETIME)
* [INDEFINITE_LIFETIME](/Java/GSSCredential/INDEFINITE_LIFETIME)
* [INITIATE_AND_ACCEPT](/Java/GSSCredential/INITIATE_AND_ACCEPT)
* [INITIATE_ONLY](/Java/GSSCredential/INITIATE_ONLY)

## Métodos
* [add()](/Java/GSSCredential/add)
* [dispose()](/Java/GSSCredential/dispose)
* [equals()](/Java/GSSCredential/equals)
* [getMechs()](/Java/GSSCredential/getMechs)
* [getName()](/Java/GSSCredential/getName)
* [getRemainingAcceptLifetime()](/Java/GSSCredential/getRemainingAcceptLifetime)
* [getRemainingInitLifetime()](/Java/GSSCredential/getRemainingInitLifetime)
* [getRemainingLifetime()](/Java/GSSCredential/getRemainingLifetime)
* [getUsage()](/Java/GSSCredential/getUsage)
* [hashCode()](/Java/GSSCredential/hashCode)

## Ejemplo
~~~java
{{ site.data.Java.G.GSSCredential.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.G.GSSCredential.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
