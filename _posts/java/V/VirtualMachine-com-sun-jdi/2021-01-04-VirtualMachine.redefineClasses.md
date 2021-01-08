---
title: VirtualMachine.redefineClasses()
permalink: Java/VirtualMachine-com-sun-jdi/redefineClasses
date: 2021-01-04
key: JavaJava.V.VirtualMachine-com-sun-jdi
category: java
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
* **Map&lt;? extends ReferenceType**,  {% include w3api/param_description.html metodo=_data parametro="Map<? extends ReferenceType" %}
* **byte[]&gt; classToBytes**,  {% include w3api/param_description.html metodo=_data parametro="byte[]> classToBytes" %}

## Excepciones
[UnsupportedOperationException](/Java/UnsupportedOperationException/), [VMCannotBeModifiedException](/Java/VMCannotBeModifiedException/)

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
