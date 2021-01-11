---
title: JTextComponent.print()
permalink: Java/JTextComponent/print
date: 2021-01-11
key: JavaJava.J.JTextComponent
category: java
tags: ['java se', 'javax.swing.text', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JTextComponent.metodos valor="print" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean print() throws PrinterException
public boolean print(MessageFormat headerFormat, MessageFormat footerFormat) throws PrinterException
public boolean print(MessageFormat headerFormat, MessageFormat footerFormat, boolean showPrintDialog, PrintService service, PrintRequestAttributeSet attributes, boolean interactive) throws PrinterException
~~~

## Parámetros
* **boolean showPrintDialog**,  {% include w3api/param_description.html metodo=_dato parametro="boolean showPrintDialog" %}
* **boolean interactive**,  {% include w3api/param_description.html metodo=_dato parametro="boolean interactive" %}
* **MessageFormat footerFormat**,  {% include w3api/param_description.html metodo=_dato parametro="MessageFormat footerFormat" %}
* **PrintService service**,  {% include w3api/param_description.html metodo=_dato parametro="PrintService service" %}
* **PrintRequestAttributeSet attributes**,  {% include w3api/param_description.html metodo=_dato parametro="PrintRequestAttributeSet attributes" %}
* **MessageFormat headerFormat**,  {% include w3api/param_description.html metodo=_dato parametro="MessageFormat headerFormat" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [PrinterException](/Java/PrinterException/)

## Clase Padre
[JTextComponent](/Java/JTextComponent/)

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
