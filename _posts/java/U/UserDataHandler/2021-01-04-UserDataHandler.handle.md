---
title: UserDataHandler.handle()
permalink: Java/UserDataHandler/handle
date: 2021-01-04
key: JavaJava.U.UserDataHandler
category: java
tags: ['java se', 'org.w3c.dom', 'java.xml', 'metodo java', 'Java 1.5', 'DOM Level 3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.U.UserDataHandler.metodos valor="handle" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void handle(short operation, String key, Object data, Node src, Node dst)
~~~

## Parámetros
* **Node dst**,  {% include w3api/param_description.html metodo=_data parametro="Node dst" %}
* **Object data**,  {% include w3api/param_description.html metodo=_data parametro="Object data" %}
* **short operation**,  {% include w3api/param_description.html metodo=_data parametro="short operation" %}
* **String key**,  {% include w3api/param_description.html metodo=_data parametro="String key" %}
* **Node src**,  {% include w3api/param_description.html metodo=_data parametro="Node src" %}

## Clase Padre
[UserDataHandler](/Java/UserDataHandler/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.U.UserDataHandler.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
