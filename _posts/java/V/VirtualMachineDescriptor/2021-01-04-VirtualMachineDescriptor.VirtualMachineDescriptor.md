---
title: VirtualMachineDescriptor.VirtualMachineDescriptor()
permalink: Java/VirtualMachineDescriptor/VirtualMachineDescriptor
date: 2021-01-04
key: JavaJava.V.VirtualMachineDescriptor
category: java
tags: ['java se', 'com.sun.tools.attach', 'jdk.attach', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.V.VirtualMachineDescriptor.constructores valor="VirtualMachineDescriptor" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public VirtualMachineDescriptor(AttachProvider provider, String id)
public VirtualMachineDescriptor(AttachProvider provider, String id, String displayName)
~~~

## Parámetros
* **String id**,  {% include w3api/param_description.html metodo=_data parametro="String id" %}
* **String displayName**,  {% include w3api/param_description.html metodo=_data parametro="String displayName" %}
* **AttachProvider provider**,  {% include w3api/param_description.html metodo=_data parametro="AttachProvider provider" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[VirtualMachineDescriptor](/Java/VirtualMachineDescriptor/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.V.VirtualMachineDescriptor.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
