---
title: ValueHandler.readValue()
permalink: Java/ValueHandler/readValue
date: 2021-01-04
key: JavaJava.V.ValueHandler
category: java
tags: ['java se', 'javax.rmi.CORBA', 'java.corba', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.V.ValueHandler.metodos valor="readValue" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Serializable readValue(InputStream in, int offset, Class clz, String repositoryID, RunTime sender)
~~~

## Parámetros
* **RunTime sender**,  {% include w3api/param_description.html metodo=_data parametro="RunTime sender" %}
* **InputStream in**,  {% include w3api/param_description.html metodo=_data parametro="InputStream in" %}
* **String repositoryID**,  {% include w3api/param_description.html metodo=_data parametro="String repositoryID" %}
* **int offset**,  {% include w3api/param_description.html metodo=_data parametro="int offset" %}
* **Class clz**,  {% include w3api/param_description.html metodo=_data parametro="Class clz" %}

## Clase Padre
[ValueHandler](/Java/ValueHandler/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.V.ValueHandler.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
