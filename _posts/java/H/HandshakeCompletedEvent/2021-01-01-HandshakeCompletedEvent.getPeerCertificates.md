---
title: HandshakeCompletedEvent.getPeerCertificates()
permalink: /Java/HandshakeCompletedEvent/getPeerCertificates/
date: 2021-01-11
key: Java.H.HandshakeCompletedEvent
category: Java
tags: ['java se', 'javax.net.ssl', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HandshakeCompletedEvent.metodos valor="getPeerCertificates" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Certificate[] getPeerCertificates() throws SSLPeerUnverifiedException
~~~

## Excepciones
[SSLPeerUnverifiedException](/Java/SSLPeerUnverifiedException/)

## Clase Padre
[HandshakeCompletedEvent](/Java/HandshakeCompletedEvent/)

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
