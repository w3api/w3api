---
title: URLStreamHandler.setURL()
permalink: Java/URLStreamHandler/setURL
date: 2021-01-11
key: JavaJava.U.URLStreamHandler
category: java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.U.URLStreamHandler.metodos valor="setURL" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@Deprecated protected void setURL(URL u, String protocol, String host, int port, String file, String ref)
protected void setURL(URL u, String protocol, String host, int port, String authority, String userInfo, String path, String query, String ref)
~~~

## Parámetros
* **String file**,  {% include w3api/param_description.html metodo=_dato parametro="String file" %}
* **String path**,  {% include w3api/param_description.html metodo=_dato parametro="String path" %}
* **String authority**,  {% include w3api/param_description.html metodo=_dato parametro="String authority" %}
* **URL u**,  {% include w3api/param_description.html metodo=_dato parametro="URL u" %}
* **String ref**,  {% include w3api/param_description.html metodo=_dato parametro="String ref" %}
* **String host**,  {% include w3api/param_description.html metodo=_dato parametro="String host" %}
* **int port**,  {% include w3api/param_description.html metodo=_dato parametro="int port" %}
* **String query**,  {% include w3api/param_description.html metodo=_dato parametro="String query" %}
* **String userInfo**,  {% include w3api/param_description.html metodo=_dato parametro="String userInfo" %}
* **String protocol**,  {% include w3api/param_description.html metodo=_dato parametro="String protocol" %}

## Excepciones
[SecurityException](/Java/SecurityException/)

## Clase Padre
[URLStreamHandler](/Java/URLStreamHandler/)

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
