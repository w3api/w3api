---
title: HttpsURLConnection.getPeerPrincipal()
permalink: Java/HttpsURLConnection/getPeerPrincipal
date: 2021-01-11
key: JavaJava.H.HttpsURLConnection
category: java
tags: ['java se', 'javax.net.ssl', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HttpsURLConnection.metodos valor="getPeerPrincipal" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Principal getPeerPrincipal() throws SSLPeerUnverifiedException
~~~

## Excepciones
[SSLPeerUnverifiedException](/Java/SSLPeerUnverifiedException/), [IllegalStateException](/Java/IllegalStateException/)

## Clase Padre
[HttpsURLConnection](/Java/HttpsURLConnection/)

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
