---
title: VirtualMachine.mirrorOf()
permalink: Java/VirtualMachine-com-sun-jdi/mirrorOf
date: 2021-01-04
key: JavaJava.V.VirtualMachine-com-sun-jdi
category: java
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
* **float value**,  {% include w3api/param_description.html metodo=_data parametro="float value" %}
* **byte value**,  {% include w3api/param_description.html metodo=_data parametro="byte value" %}
* **char value**,  {% include w3api/param_description.html metodo=_data parametro="char value" %}
* **long value**,  {% include w3api/param_description.html metodo=_data parametro="long value" %}
* **String value**,  {% include w3api/param_description.html metodo=_data parametro="String value" %}
* **double value**,  {% include w3api/param_description.html metodo=_data parametro="double value" %}
* **boolean value**,  {% include w3api/param_description.html metodo=_data parametro="boolean value" %}
* **short value**,  {% include w3api/param_description.html metodo=_data parametro="short value" %}
* **int value**,  {% include w3api/param_description.html metodo=_data parametro="int value" %}

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
{%- for _ldc in site.data.Java.V.VirtualMachine-com-sun-jdi.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
