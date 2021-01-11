---
title: GSSException.setMinor()
permalink: Java/GSSException/setMinor
date: 2021-01-11
key: JavaJava.G.GSSException
category: java
tags: ['java se', 'org.ietf.jgss', 'java.security.jgss', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.G.GSSException.metodos valor="setMinor" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setMinor(int minorCode, String message)
~~~

## Parámetros
* **String message**,  {% include w3api/param_description.html metodo=_dato parametro="String message" %}
* **int minorCode**,  {% include w3api/param_description.html metodo=_dato parametro="int minorCode" %}

## Clase Padre
[GSSException](/Java/GSSException/)

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
