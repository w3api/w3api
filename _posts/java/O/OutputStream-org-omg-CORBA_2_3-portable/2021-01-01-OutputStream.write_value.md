---
title: OutputStream.write_value()
permalink: /Java/OutputStream-org-omg-CORBA_2_3-portable/write_value/
date: 2021-01-11
key: Java.O.OutputStream-org-omg-CORBA_2_3-portable
category: Java
tags: ['java se', 'org.omg.CORBA_2_3.portable', 'java.corba', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.OutputStream-org-omg-CORBA_2_3-portable.metodos valor="write_value" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void write_value(Serializable value)
public void write_value(Serializable value, Class clz)
public void write_value(Serializable value, String repository_id)
public void write_value(Serializable value, BoxedValueHelper factory)
~~~

## Parámetros
* **BoxedValueHelper factory**,  {% include w3api/param_description.html metodo=_dato parametro="BoxedValueHelper factory" %}
* **String repository_id**,  {% include w3api/param_description.html metodo=_dato parametro="String repository_id" %}
* **Serializable value**,  {% include w3api/param_description.html metodo=_dato parametro="Serializable value" %}
* **Class clz**,  {% include w3api/param_description.html metodo=_dato parametro="Class clz" %}

## Clase Padre
[OutputStream](/Java/OutputStream-org-omg-CORBA_2_3-portable/)

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
