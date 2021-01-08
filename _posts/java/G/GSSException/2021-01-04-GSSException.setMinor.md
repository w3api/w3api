---
title: GSSException.setMinor()
permalink: Java/GSSException/setMinor
date: 2021-01-04
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
* **String message**,  {% include w3api/param_description.html metodo=_data parametro="String message" %}
* **int minorCode**,  {% include w3api/param_description.html metodo=_data parametro="int minorCode" %}

## Clase Padre
[GSSException](/Java/GSSException/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.G.GSSException.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
