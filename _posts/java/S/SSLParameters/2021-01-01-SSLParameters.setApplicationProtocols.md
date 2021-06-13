---
title: SSLParameters.setApplicationProtocols()
permalink: /Java/SSLParameters/setApplicationProtocols/
date: 2021-01-11
key: Java.S.SSLParameters
category: Java
tags: ['java se', 'javax.net.ssl', 'java.base', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SSLParameters.metodos valor="setApplicationProtocols" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setApplicationProtocols(String[] protocols)
~~~

## Parámetros
* **String[] protocols**,  {% include w3api/param_description.html metodo=_dato parametro="String[] protocols" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[SSLParameters](/Java/SSLParameters/)

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
