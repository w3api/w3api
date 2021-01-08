---
title: DataHandler.DataHandler()
permalink: Java/DataHandler/DataHandler
date: 2021-01-04
key: JavaJava.D.DataHandler
category: java
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
* **URL url**,  {% include w3api/param_description.html metodo=_data parametro="URL url" %}
* **String mimeType**,  {% include w3api/param_description.html metodo=_data parametro="String mimeType" %}
* **Object obj**,  {% include w3api/param_description.html metodo=_data parametro="Object obj" %}
* **DataSource ds**,  {% include w3api/param_description.html metodo=_data parametro="DataSource ds" %}

## Clase Padre
[DataHandler](/Java/DataHandler/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DataHandler.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
