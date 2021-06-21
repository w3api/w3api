---
title: IORInterceptor_3_0Operations.adapter_state_changed()
permalink: /Java/IORInterceptor_3_0Operations/adapter_state_changed/
date: 2021-01-11
key: Java.I.IORInterceptor_3_0Operations
category: Java
tags: ['java se', 'org.omg.PortableInterceptor', 'java.corba', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IORInterceptor_3_0Operations.metodos valor="adapter_state_changed" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void adapter_state_changed(ObjectReferenceTemplate[] templates, short state)
~~~

## Parámetros
* **short state**,  {% include w3api/param_description.html metodo=_dato parametro="short state" %}
* **ObjectReferenceTemplate[] templates**,  {% include w3api/param_description.html metodo=_dato parametro="ObjectReferenceTemplate[] templates" %}

## Clase Padre
[IORInterceptor_3_0Operations](/Java/IORInterceptor_3_0Operations/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
