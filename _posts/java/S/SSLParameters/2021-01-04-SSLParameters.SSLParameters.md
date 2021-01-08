---
title: SSLParameters.SSLParameters()
permalink: Java/SSLParameters/SSLParameters
date: 2021-01-04
key: JavaJava.S.SSLParameters
category: java
tags: ['java se', 'javax.net.ssl', 'java.base', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SSLParameters.constructores valor="SSLParameters" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public SSLParameters()
public SSLParameters(String[] cipherSuites)
public SSLParameters(String[] cipherSuites, String[] protocols)
~~~

## Parámetros
* **String[] cipherSuites**,  {% include w3api/param_description.html metodo=_data parametro="String[] cipherSuites" %}
* **String[] protocols**,  {% include w3api/param_description.html metodo=_data parametro="String[] protocols" %}

## Clase Padre
[SSLParameters](/Java/SSLParameters/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SSLParameters.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
