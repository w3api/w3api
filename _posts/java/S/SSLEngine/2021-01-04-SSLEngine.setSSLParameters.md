---
title: SSLEngine.setSSLParameters()
permalink: Java/SSLEngine/setSSLParameters
date: 2021-01-04
key: JavaJava.S.SSLEngine
category: java
tags: ['java se', 'javax.net.ssl', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SSLEngine.metodos valor="setSSLParameters" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setSSLParameters(SSLParameters params)
~~~

## Parámetros
* **SSLParameters params**,  {% include w3api/param_description.html metodo=_data parametro="SSLParameters params" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[SSLEngine](/Java/SSLEngine/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SSLEngine.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
