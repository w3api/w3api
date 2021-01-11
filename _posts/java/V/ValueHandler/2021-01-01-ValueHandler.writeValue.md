---
title: ValueHandler.writeValue()
permalink: Java/ValueHandler/writeValue
date: 2021-01-11
key: JavaJava.V.ValueHandler
category: java
tags: ['java se', 'javax.rmi.CORBA', 'java.corba', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.V.ValueHandler.metodos valor="writeValue" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void writeValue(OutputStream out, Serializable value)
~~~

## Parámetros
* **OutputStream out**,  {% include w3api/param_description.html metodo=_dato parametro="OutputStream out" %}
* **Serializable value**,  {% include w3api/param_description.html metodo=_dato parametro="Serializable value" %}

## Clase Padre
[ValueHandler](/Java/ValueHandler/)

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
