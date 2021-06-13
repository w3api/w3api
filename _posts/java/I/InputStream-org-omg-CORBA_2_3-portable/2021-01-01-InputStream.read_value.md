---
title: InputStream.read_value()
permalink: /Java/InputStream-org-omg-CORBA_2_3-portable/read_value/
date: 2021-01-11
key: Java.I.InputStream-org-omg-CORBA_2_3-portable
category: Java
tags: ['java se', 'org.omg.CORBA_2_3.portable', 'java.corba', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.InputStream-org-omg-CORBA_2_3-portable.metodos valor="read_value" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Serializable read_value()
public Serializable read_value(Serializable value)
public Serializable read_value(Class clz)
public Serializable read_value(String rep_id)
public Serializable read_value(BoxedValueHelper factory)
~~~

## Parámetros
* **BoxedValueHelper factory**,  {% include w3api/param_description.html metodo=_dato parametro="BoxedValueHelper factory" %}
* **Serializable value**,  {% include w3api/param_description.html metodo=_dato parametro="Serializable value" %}
* **String rep_id**,  {% include w3api/param_description.html metodo=_dato parametro="String rep_id" %}
* **Class clz**,  {% include w3api/param_description.html metodo=_dato parametro="Class clz" %}

## Clase Padre
[InputStream](/Java/InputStream-org-omg-CORBA_2_3-portable/)

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
