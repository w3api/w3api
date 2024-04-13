---
title: VirtualMachine.mirrorOf()
permalink: /Java/VirtualMachine-com-sun-jdi/mirrorOf/
date: 2021-01-11
key: Java.V.VirtualMachine-com-sun-jdi
category: Java
tags: ['java se', 'com.sun.jdi', 'jdk.jdi', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.V.VirtualMachine-com-sun-jdi.metodos valor="mirrorOf" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
BooleanValue mirrorOf(boolean value)
ByteValue mirrorOf(byte value)
CharValue mirrorOf(char value)
DoubleValue mirrorOf(double value)
FloatValue mirrorOf(float value)
IntegerValue mirrorOf(int value)
LongValue mirrorOf(long value)
ShortValue mirrorOf(short value)
StringReference mirrorOf(String value)
~~~

## Parámetros
* **byte value**,  {% include w3api/param_description.html metodo=_dato parametro="byte value" %}
* **int value**,  {% include w3api/param_description.html metodo=_dato parametro="int value" %}
* **char value**,  {% include w3api/param_description.html metodo=_dato parametro="char value" %}
* **double value**,  {% include w3api/param_description.html metodo=_dato parametro="double value" %}
* **long value**,  {% include w3api/param_description.html metodo=_dato parametro="long value" %}
* **short value**,  {% include w3api/param_description.html metodo=_dato parametro="short value" %}
* **String value**,  {% include w3api/param_description.html metodo=_dato parametro="String value" %}
* **boolean value**,  {% include w3api/param_description.html metodo=_dato parametro="boolean value" %}
* **float value**,  {% include w3api/param_description.html metodo=_dato parametro="float value" %}

## Excepciones
[VMCannotBeModifiedException](/Java/VMCannotBeModifiedException/)

## Clase Padre
[VirtualMachine](/Java/VirtualMachine-com-sun-jdi/)

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
