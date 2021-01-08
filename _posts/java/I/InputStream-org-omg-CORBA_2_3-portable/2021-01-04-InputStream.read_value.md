---
title: InputStream.read_value()
permalink: Java/InputStream-org-omg-CORBA_2_3-portable/read_value
date: 2021-01-04
key: JavaJava.I.InputStream-org-omg-CORBA_2_3-portable
category: java
tags: ['java se', 'org.omg.CORBA_2_3.portable', 'java.corba', 'metodo java', 'JDKJava 1.2']
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
* **Serializable value**,  {% include w3api/param_description.html metodo=_data parametro="Serializable value" %}
* **Class clz**,  {% include w3api/param_description.html metodo=_data parametro="Class clz" %}
* **String rep_id**,  {% include w3api/param_description.html metodo=_data parametro="String rep_id" %}
* **BoxedValueHelper factory**,  {% include w3api/param_description.html metodo=_data parametro="BoxedValueHelper factory" %}

## Clase Padre
[InputStream](/Java/InputStream-org-omg-CORBA_2_3-portable/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.InputStream-org-omg-CORBA_2_3-portable.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
