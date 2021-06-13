---
title: SSLSession.getPeerCertificateChain()
permalink: /Java/SSLSession/getPeerCertificateChain/
date: 2021-01-11
key: Java.S.SSLSession
category: Java
tags: ['java se', 'javax.net.ssl', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SSLSession.metodos valor="getPeerCertificateChain" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@Deprecated(since="9") X509Certificate[] getPeerCertificateChain() throws SSLPeerUnverifiedException
~~~

## Excepciones
[SSLPeerUnverifiedException](/Java/SSLPeerUnverifiedException/)

## Clase Padre
[SSLSession](/Java/SSLSession/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
