---
title: SSLSession.getPeerPrincipal()
permalink: Java/SSLSession/getPeerPrincipal
date: 2021-01-04
key: JavaJava.S.SSLSession
category: java
tags: ['java se', 'javax.net.ssl', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SSLSession.metodos valor="getPeerPrincipal" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Principal getPeerPrincipal() throws SSLPeerUnverifiedException
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
{%- for _ldc in site.data.Java.S.SSLSession.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
