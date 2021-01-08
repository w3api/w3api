---
title: AbstractJSObject.getDefaultValue()
permalink: Java/AbstractJSObject/getDefaultValue
date: 2021-01-04
key: JavaJava.A.AbstractJSObject
category: java
tags: ['java se', 'jdk.nashorn.api.scripting', 'jdk.scripting.nashorn', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AbstractJSObject.metodos valor="getDefaultValue" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@Deprecated public static Object getDefaultValue(JSObject jsobj, Class<?> hint)
~~~

## Parámetros
* **JSObject jsobj**,  {% include w3api/param_description.html metodo=_data parametro="JSObject jsobj" %}
* **Class&lt;?&gt; hint**,  {% include w3api/param_description.html metodo=_data parametro="Class<?> hint" %}

## Excepciones
[UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[AbstractJSObject](/Java/AbstractJSObject/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AbstractJSObject.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
