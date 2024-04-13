---
title: DataHandler.DataHandler()
permalink: /Java/DataHandler/DataHandler/
date: 2021-01-11
key: Java.D.DataHandler
category: Java
tags: ['java se', 'javax.activation', 'java.activation', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DataHandler.constructores valor="DataHandler" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public DataHandler(Object obj, String mimeType)
public DataHandler(URL url)
public DataHandler(DataSource ds)
~~~

## Parámetros
* **URL url**,  {% include w3api/param_description.html metodo=_dato parametro="URL url" %}
* **String mimeType**,  {% include w3api/param_description.html metodo=_dato parametro="String mimeType" %}
* **Object obj**,  {% include w3api/param_description.html metodo=_dato parametro="Object obj" %}
* **DataSource ds**,  {% include w3api/param_description.html metodo=_dato parametro="DataSource ds" %}

## Clase Padre
[DataHandler](/Java/DataHandler/)

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
