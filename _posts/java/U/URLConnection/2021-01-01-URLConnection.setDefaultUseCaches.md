---
title: URLConnection.setDefaultUseCaches()
permalink: /Java/URLConnection/setDefaultUseCaches/
date: 2021-01-11
key: Java.U.URLConnection
category: Java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.U.URLConnection.metodos valor="setDefaultUseCaches" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setDefaultUseCaches(boolean defaultusecaches)
public static void setDefaultUseCaches(String protocol, boolean defaultVal)
~~~

## Parámetros
* **String protocol**,  {% include w3api/param_description.html metodo=_dato parametro="String protocol" %}
* **boolean defaultVal**,  {% include w3api/param_description.html metodo=_dato parametro="boolean defaultVal" %}
* **boolean defaultusecaches**,  {% include w3api/param_description.html metodo=_dato parametro="boolean defaultusecaches" %}

## Clase Padre
[URLConnection](/Java/URLConnection/)

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
