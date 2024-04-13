---
title: ValueHandlerMultiFormat.writeValue()
permalink: /Java/ValueHandlerMultiFormat/writeValue/
date: 2021-01-11
key: Java.V.ValueHandlerMultiFormat
category: Java
tags: ['java se', 'javax.rmi.CORBA', 'java.corba', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.V.ValueHandlerMultiFormat.metodos valor="writeValue" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void writeValue(OutputStream out, Serializable value, byte streamFormatVersion)
~~~

## Parámetros
* **OutputStream out**,  {% include w3api/param_description.html metodo=_dato parametro="OutputStream out" %}
* **Serializable value**,  {% include w3api/param_description.html metodo=_dato parametro="Serializable value" %}
* **byte streamFormatVersion**,  {% include w3api/param_description.html metodo=_dato parametro="byte streamFormatVersion" %}

## Clase Padre
[ValueHandlerMultiFormat](/Java/ValueHandlerMultiFormat/)

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
