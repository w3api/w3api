---
title: VirtualMachine.redefineClasses()
permalink: /Java/VirtualMachine-com-sun-jdi/redefineClasses/
date: 2021-01-11
key: Java.V.VirtualMachine-com-sun-jdi
category: Java
tags: ['java se', 'com.sun.jdi', 'jdk.jdi', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.V.VirtualMachine-com-sun-jdi.metodos valor="redefineClasses" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void redefineClasses(Map<? extends ReferenceType,byte[]> classToBytes)
~~~

## Parámetros
* **byte[]&gt; classToBytes**,  {% include w3api/param_description.html metodo=_dato parametro="byte[]> classToBytes" %}
* **Map&lt;? extends ReferenceType**,  {% include w3api/param_description.html metodo=_dato parametro="Map<? extends ReferenceType" %}

## Excepciones
[VMCannotBeModifiedException](/Java/VMCannotBeModifiedException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

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
