---
title: CompoundName.CompoundName()
permalink: /Java/CompoundName/CompoundName/
date: 2021-01-11
key: Java.C.CompoundName
category: Java
tags: ['java se', 'javax.naming', 'java.naming', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CompoundName.constructores valor="CompoundName" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public CompoundName(String n, Properties syntax) throws InvalidNameException
protected CompoundName(Enumeration<String> comps, Properties syntax)
~~~

## Parámetros
* **String n**,  {% include w3api/param_description.html metodo=_dato parametro="String n" %}
* **Properties syntax**,  {% include w3api/param_description.html metodo=_dato parametro="Properties syntax" %}
* **Enumeration&lt;String&gt; comps**,  {% include w3api/param_description.html metodo=_dato parametro="Enumeration<String> comps" %}

## Excepciones
[InvalidNameException](/Java/InvalidNameException/)

## Clase Padre
[CompoundName](/Java/CompoundName/)

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
