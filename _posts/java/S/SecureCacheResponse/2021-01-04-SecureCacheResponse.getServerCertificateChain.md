---
title: SecureCacheResponse.getServerCertificateChain()
permalink: Java/SecureCacheResponse/getServerCertificateChain
date: 2021-01-04
key: JavaJava.S.SecureCacheResponse
category: java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SecureCacheResponse.metodos valor="getServerCertificateChain" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract List<Certificate> getServerCertificateChain() throws SSLPeerUnverifiedException
~~~

## Excepciones
[SSLPeerUnverifiedException](/Java/SSLPeerUnverifiedException/)

## Clase Padre
[SecureCacheResponse](/Java/SecureCacheResponse/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SecureCacheResponse.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
