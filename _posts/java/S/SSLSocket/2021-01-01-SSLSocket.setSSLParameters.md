---
title: SSLSocket.setSSLParameters()
permalink: /Java/SSLSocket/setSSLParameters/
date: 2021-01-11
key: Java.S.SSLSocket
category: Java
tags: ['java se', 'javax.net.ssl', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SSLSocket.metodos valor="setSSLParameters" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setSSLParameters(SSLParameters params)
~~~

## Parámetros
* **SSLParameters params**,  {% include w3api/param_description.html metodo=_dato parametro="SSLParameters params" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[SSLSocket](/Java/SSLSocket/)

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
