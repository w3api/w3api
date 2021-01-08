---
title: VirtualMachine.instanceCounts()
permalink: Java/VirtualMachine-com-sun-jdi/instanceCounts
date: 2021-01-04
key: JavaJava.V.VirtualMachine-com-sun-jdi
category: java
tags: ['java se', 'com.sun.jdi', 'jdk.jdi', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.V.VirtualMachine-com-sun-jdi.metodos valor="instanceCounts" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
long[] instanceCounts(List<? extends ReferenceType> refTypes)
~~~

## Parámetros
* **List&lt;? extends ReferenceType&gt; refTypes**,  {% include w3api/param_description.html metodo=_data parametro="List<? extends ReferenceType> refTypes" %}

## Excepciones
[UnsupportedOperationException](/Java/UnsupportedOperationException/), [NullPointerException](/Java/NullPointerException/)

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
