---
title: InvokeHandler._invoke()
permalink: Java/InvokeHandler/_invoke
date: 2021-01-04
key: JavaJava.I.InvokeHandler
category: java
tags: ['java se', 'org.omg.CORBA.portable', 'java.corba', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.InvokeHandler.metodos valor="_invoke" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
OutputStream _invoke(String method, InputStream input, ResponseHandler handler) throws SystemException
~~~

## Parámetros
* **InputStream input**,  {% include w3api/param_description.html metodo=_data parametro="InputStream input" %}
* **ResponseHandler handler**,  {% include w3api/param_description.html metodo=_data parametro="ResponseHandler handler" %}
* **String method**,  {% include w3api/param_description.html metodo=_data parametro="String method" %}

## Excepciones
[SystemException](/Java/SystemException/)

## Clase Padre
[InvokeHandler](/Java/InvokeHandler/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.InvokeHandler.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
