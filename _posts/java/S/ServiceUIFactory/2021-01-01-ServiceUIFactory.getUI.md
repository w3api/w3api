---
title: ServiceUIFactory.getUI()
permalink: Java/ServiceUIFactory/getUI
date: 2021-01-11
key: JavaJava.S.ServiceUIFactory
category: java
tags: ['java se', 'javax.print', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.ServiceUIFactory.metodos valor="getUI" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract Object getUI(int role, String ui)
~~~

## Parámetros
* **int role**,  {% include w3api/param_description.html metodo=_dato parametro="int role" %}
* **String ui**,  {% include w3api/param_description.html metodo=_dato parametro="String ui" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ServiceUIFactory](/Java/ServiceUIFactory/)

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
