---
title: VirtualMachine.VirtualMachine()
permalink: Java/VirtualMachine-com-sun-tools-attach/VirtualMachine
date: 2021-01-11
key: JavaJava.V.VirtualMachine-com-sun-tools-attach
category: java
tags: ['java se', 'com.sun.tools.attach', 'jdk.attach', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.V.VirtualMachine-com-sun-tools-attach.constructores valor="VirtualMachine" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected VirtualMachine(AttachProvider provider, String id)
~~~

## Parámetros
* **AttachProvider provider**,  {% include w3api/param_description.html metodo=_dato parametro="AttachProvider provider" %}
* **String id**,  {% include w3api/param_description.html metodo=_dato parametro="String id" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[VirtualMachine](/Java/VirtualMachine-com-sun-tools-attach/)

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
