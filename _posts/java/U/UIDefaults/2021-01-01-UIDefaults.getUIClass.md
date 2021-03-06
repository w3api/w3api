---
title: UIDefaults.getUIClass()
permalink: /Java/UIDefaults/getUIClass/
date: 2021-01-11
key: Java.U.UIDefaults
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.U.UIDefaults.metodos valor="getUIClass" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Class<? extends ComponentUI> getUIClass(String uiClassID)
public Class<? extends ComponentUI> getUIClass(String uiClassID, ClassLoader uiClassLoader)
~~~

## Parámetros
* **ClassLoader uiClassLoader**,  {% include w3api/param_description.html metodo=_dato parametro="ClassLoader uiClassLoader" %}
* **String uiClassID**,  {% include w3api/param_description.html metodo=_dato parametro="String uiClassID" %}

## Clase Padre
[UIDefaults](/Java/UIDefaults/)

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
