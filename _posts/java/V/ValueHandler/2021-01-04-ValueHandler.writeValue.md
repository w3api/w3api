---
title: ValueHandler.writeValue()
permalink: Java/ValueHandler/writeValue
date: 2021-01-04
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
* **Serializable value**,  {% include w3api/param_description.html metodo=_data parametro="Serializable value" %}
* **OutputStream out**,  {% include w3api/param_description.html metodo=_data parametro="OutputStream out" %}

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
