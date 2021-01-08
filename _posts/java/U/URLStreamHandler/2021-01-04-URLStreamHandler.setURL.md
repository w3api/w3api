---
title: URLStreamHandler.setURL()
permalink: Java/URLStreamHandler/setURL
date: 2021-01-04
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
* **String file**,  {% include w3api/param_description.html metodo=_data parametro="String file" %}
* **String authority**,  {% include w3api/param_description.html metodo=_data parametro="String authority" %}
* **String host**,  {% include w3api/param_description.html metodo=_data parametro="String host" %}
* **String protocol**,  {% include w3api/param_description.html metodo=_data parametro="String protocol" %}
* **URL u**,  {% include w3api/param_description.html metodo=_data parametro="URL u" %}
* **int port**,  {% include w3api/param_description.html metodo=_data parametro="int port" %}
* **String query**,  {% include w3api/param_description.html metodo=_data parametro="String query" %}
* **String userInfo**,  {% include w3api/param_description.html metodo=_data parametro="String userInfo" %}
* **String path**,  {% include w3api/param_description.html metodo=_data parametro="String path" %}
* **String ref**,  {% include w3api/param_description.html metodo=_data parametro="String ref" %}

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
{%- for _ldc in site.data.Java.U.URLStreamHandler.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
