---
title: OutputStream.write_value()
permalink: Java/OutputStream-org-omg-CORBA_2_3-portable/write_value
date: 2021-01-04
key: JavaJava.O.OutputStream-org-omg-CORBA_2_3-portable
category: java
tags: ['java se', 'org.omg.CORBA_2_3.portable', 'java.corba', 'metodo java', 'JDKJava 1.2']
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
* **Serializable value**,  {% include w3api/param_description.html metodo=_data parametro="Serializable value" %}
* **Class clz**,  {% include w3api/param_description.html metodo=_data parametro="Class clz" %}
* **String repository_id**,  {% include w3api/param_description.html metodo=_data parametro="String repository_id" %}
* **BoxedValueHelper factory**,  {% include w3api/param_description.html metodo=_data parametro="BoxedValueHelper factory" %}

## Clase Padre
[OutputStream](/Java/OutputStream-org-omg-CORBA_2_3-portable/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.O.OutputStream-org-omg-CORBA_2_3-portable.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
