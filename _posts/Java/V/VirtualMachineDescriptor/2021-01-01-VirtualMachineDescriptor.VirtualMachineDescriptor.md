---
title: VirtualMachineDescriptor.VirtualMachineDescriptor()
permalink: /Java/VirtualMachineDescriptor/VirtualMachineDescriptor/
date: 2021-01-11
key: Java.V.VirtualMachineDescriptor
category: Java
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
* **AttachProvider provider**,  {% include w3api/param_description.html metodo=_dato parametro="AttachProvider provider" %}
* **String id**,  {% include w3api/param_description.html metodo=_dato parametro="String id" %}
* **String displayName**,  {% include w3api/param_description.html metodo=_dato parametro="String displayName" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
