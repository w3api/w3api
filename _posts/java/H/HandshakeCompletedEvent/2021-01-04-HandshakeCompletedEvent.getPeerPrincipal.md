---
title: HandshakeCompletedEvent.getPeerPrincipal()
permalink: Java/HandshakeCompletedEvent/getPeerPrincipal
date: 2021-01-04
key: JavaJava.H.HandshakeCompletedEvent
category: java
tags: ['java se', 'javax.net.ssl', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HandshakeCompletedEvent.metodos valor="getPeerPrincipal" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Principal getPeerPrincipal() throws SSLPeerUnverifiedException
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
{%- for _ldc in site.data.Java.H.HandshakeCompletedEvent.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
