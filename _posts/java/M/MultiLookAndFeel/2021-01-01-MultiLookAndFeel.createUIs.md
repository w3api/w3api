---
title: MultiLookAndFeel.createUIs()
permalink: Java/MultiLookAndFeel/createUIs
date: 2021-01-11
key: JavaJava.M.MultiLookAndFeel
category: Java
tags: ['java se', 'javax.swing.plaf.multi', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MultiLookAndFeel.metodos valor="createUIs" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static ComponentUI createUIs(ComponentUI mui, Vector<ComponentUI> uis, JComponent target)
~~~

## Parámetros
* **JComponent target**,  {% include w3api/param_description.html metodo=_dato parametro="JComponent target" %}
* **ComponentUI mui**,  {% include w3api/param_description.html metodo=_dato parametro="ComponentUI mui" %}
* **Vector&lt;ComponentUI&gt; uis**,  {% include w3api/param_description.html metodo=_dato parametro="Vector<ComponentUI> uis" %}

## Clase Padre
[MultiLookAndFeel](/Java/MultiLookAndFeel/)

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
